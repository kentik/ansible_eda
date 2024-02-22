# Kentik Alert Notification Plugin for Ansible Event Driven Ansible

This event source plugin from Kentik accepts alert notification JSON and works in conjunction with Ansible EDA rulebooks to allow users to automate changes to their environment.

## Requirements
* Kentik portal account
* Ansible Automation Platform with EDA Controller instance

## Example rulebook
```yaml
---
- name: Listen for alerts using kentik_webhook
  hosts: all

  ## Define our source for events

  sources:
    - kentik_webhook: # for local tests only. In production use kentik.ansible_eda.kentik_webhook
        host: 0.0.0.0
        port: 80

  ## Define the conditions we are looking for

  rules:
    - name: Print out the alert
      condition: event.i == 1

      ## Define the action we should take should the condition be met

      action:
        run_playbook:
          name: playbooks/example_playbook.yml
```

## Licensing
We are using GPL 3.0 as our default.

## Additional Questions/Remarks

If you do have additional questions/remarks, feel free to reach out to Kentik support (support@kentik.com), via email.

If you think this template did not solve all your problems, please also let us know, either with a message or a pull request.
Together we can improve this template to make it easier for our future projects.