"""Verify the public November WebVoyager evidence using Python's standard library."""

import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def verify():
    root = Path(__file__).resolve().parent
    checks = (root / "SHA256SUMS.txt").read_text().splitlines()
    for line in checks:
        digest, name = line.split("  ", 1)
        require(sha((root / name).read_bytes()) == digest, name)

    def check_file(data, entry):
        require(sha(data) == entry["public_sha256"], entry["publication"])
        require(len(data) == entry["bytes"], entry["publication"])

    files = read(root / "evidence-lineage.json")
    groups = defaultdict(dict)
    for entry in files:
        archive, sep, member = entry["publication"].partition("!")
        if sep:
            require(member not in groups[archive], member)
            groups[archive][member] = entry
        else:
            check_file((root / archive).read_bytes(), entry)

    schedule = {}
    for event in map(json.loads, (root / "run/schedule.jsonl").read_bytes().splitlines()):
        key = (event["task_id"], event["event"])
        require(key not in schedule, str(key))
        schedule[key] = event
    dataset_bytes = (root / "../../evaluated-615.jsonl").read_bytes()
    dataset = {task["id"]: task for task in map(json.loads, dataset_bytes.splitlines())}
    summary = read(root / "summary.json")
    require(sha(dataset_bytes) == summary["denominator_sha256"], "Dataset hash")
    rows = read(root / "task-results.json")
    later = {row["task_id"]: row for row in read(root / "attempt-history.json")}
    require(len(later) == 7 and len(groups) == len(rows) == len(dataset) == 615, "Count")
    require(set(row["task_id"] for row in rows) == set(dataset), "Task IDs")
    require({row["evidence"] for row in rows} == set(groups), "Archive index")
    scores = Counter()
    initial = Counter()
    requests = 0
    screenshots = 0
    for row in rows:
        tid = row["task_id"]
        archive = row["evidence"]
        with ZipFile(root / archive) as z:
            names = z.namelist()
            require(len(set(names)) == len(names) and set(names) == set(groups[archive]), archive)
            for name, entry in groups[archive].items():
                check_file(z.read(name), entry)
            run = json.loads(z.read("run.json"))
            judge = json.loads(z.read("judge.json"))
            bundle = json.loads(z.read("judge_input.json"))
            require(tid == run["task"]["id"] == judge["task_id"] == bundle["task_id"], tid)
            require(bundle["prompt_sha256"] == sha((root / "judge_prompt.txt").read_bytes()), tid)
            for group in (run["model_config"], run["model_config_snapshot"]):
                require(group["worker_runtime_model"] == group["worker_runtime"]["model"] == summary["worker_model"], tid)
            budget = run["browser_budget"]
            require(budget["allowed_calls"] <= budget["max_browser_commands"] == 40, tid)
            require(budget["hard_enforced"] and budget["compliant"], tid)
            require(run["screenshot_paths"] == [im["path"] for im in bundle["images"]], tid)
            for im in bundle["images"]:
                require(sha(z.read(im["path"])) == im["sha256"], tid)
                screenshots += 1
            # The archived judge hashes refer to the files before public privacy processing.
            for path, digest in bundle["source_files"].items():
                require(groups[archive][path]["source_sha256"] == digest, tid)
            if run["status"] == "completed" and run["benchmark_contract"]["valid"]:
                req = json.loads(z.read("judge_request.json"))
                raw = json.loads(z.read("judge_raw_response.json"))
                require(req["request_count"] == judge["request_count"] == 1, tid)
                require(req["input_sha256"] == bundle["input_sha256"] == judge["input_sha256"], tid)
                require(judge["model"] == raw["model"] == summary["judge"]["model"], tid)
                decision = json.loads(raw["choices"][0]["message"]["content"])
                require(decision["verdict"] == judge["decision"]["verdict"], tid)
                require(row["judge_decision"] == judge["decision"], tid)
                outcome = judge["decision"]["verdict"]
                requests += 1
            else:
                require(judge["status"] == "skipped" and judge["request_count"] == 0, tid)
                require("judge_raw_response.json" not in names and "judge_request.json" not in names, tid)
                outcome = "run_error"
        require(row["category"] == outcome, tid)
        first = schedule[tid, "complete"]
        is_later = time(run["started_at"]) > time(first["utc"])
        require(is_later == row["later_execution_record"] == (tid in later), tid)
        if is_later:
            require(first["status"] == "error" and later[tid]["final_start_utc"] == run["started_at"], tid)
        initial["run_error" if first["status"] == "error" else outcome] += 1
        scores[outcome] += 1
    require(scores == Counter({k: v for k, v in summary["final_score"]["counts"].items() if v}), "Final scores")
    require(initial == Counter({k: v for k, v in summary["first_dispatch_score"]["counts"].items() if v}), "First dispatch")
    require(requests == 614 and screenshots == 611, "Evidence counts")
    print(f"Verified {len(rows)} tasks, {len(files)} evidence files, {requests} judge responses and {screenshots} selected screenshots.")
    print(f"Initial dispatch {initial['success']}/615 = {initial['success']/615:.2%}. Final {scores['success']}/615 = {scores['success']/615:.2%}.")


if __name__ == "__main__":
    verify()
