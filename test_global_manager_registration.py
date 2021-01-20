---
#
# Playbook to register Compute Managers with NSX Appliance
#
- hosts: 127.0.0.1
  connection: local
  become: yes
  vars_files:
    - answerfile.yml
  tasks:
    - name: Register global manager
      nsxt_global_manager_registration:
          hostname: "{{ hostname }}"
          username: "{{ username }}"
          password: "{{ password }}"
          validate_certs: "{{ validate_certs }}"
          display_name: "{{ item.display_name }}"
          mode: "{{ item.mode }}"
          connection_info:
            fqdn: "{{ item.fqdn }}"
            username: "{{ item.username }}"
            password: "{{ item.password }}"
            thumbprint: "{{ item.thumbprint }}"
          state: absent
      with_items:
        - "{{global_managers}}"
