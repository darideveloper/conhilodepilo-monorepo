# Con Hilo Depilo - Monorepo

This repository contains the dashboard and frontend subprojects.

## Local Development

We use a single shell script (`dev.sh`) to start all services simultaneously for local development. The script uses `tmux` to manage the different terminal sessions in the background.

### Prerequisites

For the `dev.sh` script to work perfectly, ensure:
1. Your folder structure matches the repository (i.e., you have folders named `dashboard`, `booking`, and `landing` in the same directory as the script).
2. You have a Python virtual environment named `venv` inside the `dashboard/` directory (`dashboard/venv`).
3. You have `tmux` installed on your system.

### Starting the Environment

To start all services, simply run:

```bash
./dev.sh
```

### Essential tmux Commands

Once the script runs, you will be "inside" a tmux session named `conhilorepilo_dev`. Here are the essential keys you need to navigate:

- **Switch Windows:** Press `Ctrl+b`, then a number (`0` for dashboard, `1` for booking, `2` for landing).
- **Next/Previous Window:** Press `Ctrl+b`, then `n` (next) or `p` (previous).
- **Detach:** Press `Ctrl+b`, then `d`. This leaves the servers running in the background and returns you to your normal terminal.
- **Re-attach:** Run the script again (`./dev.sh`) or type `tmux attach -t conhilorepilo_dev`.
- **Kill everything:** Inside tmux, press `Ctrl+b`, then type `:kill-session` and hit `Enter`.
