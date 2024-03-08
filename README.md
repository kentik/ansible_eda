# Kentik Collection for Ansible

The Kentik Collection for Ansible includes an event source plugin from Kentik accepts alert notification JSON and works in conjunction with Ansible EDA rulebooks to allow users to automate changes to their environment.

## Code of Conduct
We follow the [Ansible Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html) in all our interactions within this project.

If you encounter abusive behavior, please refer to the [policy violations](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html#policy-violations) section of the Code for information on how to raise a complaint.

## Communication

Join us on:
* Email:
    * [Support email](mailto:support@kentik.com)
* Slack:
    * [Kentik Users](https://www.kentik.com/go/kentik-community-slack-signup/): Slack workspace for all Kentik users to colloborate

For more information about communication with the Ansible community, refer to the [Ansible communication guide](https://docs.ansible.com/ansible/devel/community/communication.html).

## Contributing to this collection

<!--Describe how the community can contribute to your collection. At a minimum, fill up and include the CONTRIBUTING.md file containing how and where users can create issues to report problems or request features for this collection. List contribution requirements, including preferred workflows and necessary testing, so you can benefit from community PRs. If you are following general Ansible contributor guidelines, you can link to - [Ansible Community Guide](https://docs.ansible.com/ansible/devel/community/index.html). List the current maintainers (contributors with write or higher access to the repository). The following can be included:-->

The content of this collection is made by people like you, a community of individuals collaborating on making the world better through developing automation software.

We are actively accepting new contributors and all types of contributions are very welcome.

Don't know how to start? Refer to the [Ansible community guide](https://docs.ansible.com/ansible/devel/community/index.html)!

If you find problems, please open an issue or create a PR against the [Kentik collection repository](https://github.com/kentik/ansible_eda).

See [CONTRIBUTING.md](https://github.com/kentik/ansible_eda/blob/main/CONTRIBUTING.md) for more details.

We also use the following guidelines:

* [Collection review checklist](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_reviewing.html)
* [Ansible development guide](https://docs.ansible.com/ansible/devel/dev_guide/index.html)
* [Ansible collection development guide](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#contributing-to-collections)

## Tested with Ansible

<!-- List the versions of Ansible the collection has been tested with. Must match what is in galaxy.yml. -->
Tested with Ansible Core >= 2.14.2 versions, and the current development version of Ansible. Ansible Core versions prior to 2.14.2 are not supported.

## External requirements

<!-- List any external resources the collection depends on, for example minimum versions of an OS, libraries, or utilities. Do not list other Ansible collections here. -->

* [Kentik portal account](https://portal.kentik.com)
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

### Installing the Collection from Ansible Galaxy

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:
```bash
ansible-galaxy collection install kentik.ansible_eda
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:
```yaml
---
collections:
  - name: kentik.ansible_eda
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the `ansible` package. To upgrade the collection to the latest available version, run the following command:
```bash
ansible-galaxy collection install kentik.ansible_eda --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version `0.1.0`:

```bash
ansible-galaxy collection install kentik.ansible_eda:==1.0.1
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## Release notes
<!-- Updated using antsibull-changelog (https://github.com/ansible-community/antsibull-changelog/blob/main/docs/changelogs.md)-->

See the [changelog](https://github.com/kentik/ansible_eda/blob/main/CHANGELOG.rst).

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://github.com/kentik/ansible_eda/blob/main/LICENSE) to see the full text.

## Additional Questions/Remarks

If you do have additional questions/remarks, feel free to reach out to [Kentik support](mailto:support@kentik.com), via email.

If you think this template did not solve all your problems, please also let us know, either with a message or a pull request.
Together we can improve this template to make it easier for our future projects.