---

# Vagrant Lab Setup for Incident Response Playbook

This guide walks you through creating a basic virtual lab with Vagrant and VirtualBox to test and develop your Incident Response (IR) Playbook scripts and procedures.

---

## Why Use Vagrant?

* Automates VM provisioning with code
* Supports multiple OS (Linux, Windows)
* Easy to reset & replicate your IR lab environment
* Integrates well with Ansible for config management

---

## Prerequisites

* [Install VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Install Vagrant](https://www.vagrantup.com/downloads)

---

## Step 1: Create Your Vagrantfile

Create a `Vagrantfile` in your lab folder (e.g., `/labs/Vagrantfile`):

```ruby
# labs/Vagrantfile

Vagrant.configure("2") do |config|

  # Define a Linux VM for IR tools
  config.vm.define "linux1" do |linux|
    linux.vm.box = "ubuntu/focal64"
    linux.vm.hostname = "linux1.irlab.local"
    linux.vm.network "private_network", ip: "192.168.56.101"
    linux.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.cpus = 2
    end
  end

  # Define a Windows VM for IR scripts and testing
  config.vm.define "windows1" do |win|
    win.vm.box = "gusztavvargadr/windows-10"  # Popular Windows 10 box from Vagrant Cloud
    win.vm.hostname = "windows1.irlab.local"
    win.vm.network "private_network", ip: "192.168.56.102"
    win.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.cpus = 2
    end
  end

end
```

---

## Step 2: Start Your VMs

```bash
cd labs
vagrant up
```

This command downloads the boxes and boots your VMs.

---

## Step 3: Connect to Your VMs

* Linux VM:

  ```bash
  vagrant ssh linux1
  ```

* Windows VM (RDP):

  ```bash
  vagrant rdp windows1
  ```

  *(You might need to set up RDP credentials on first boot.)*

---

## Step 4: Provision Your Environment

You can manually install tools or automate via Ansible:

```bash
ansible-playbook -i inventory.ini labs/ansible_config.yml
```

*(Ensure you have your inventory file pointing to your VMs.)*

---

## Step 5: Test Your IR Playbook & Scripts

* Run `/scripts/linux` Python tools on the Linux VM
* Run `/scripts/windows` PowerShell scripts on the Windows VM
* Use `/docs` templates and checklists as real incident guides

---

## Tips

* Snapshots: Take snapshots of your VMs to quickly revert
* Networking: Use bridged adapters for real network testing (modify `Vagrantfile`)
* Shared folders: Configure synced folders in the `Vagrantfile` to share scripts easily

---

## Resources

* [Vagrant Documentation](https://www.vagrantup.com/docs)
* [VirtualBox Docs](https://www.virtualbox.org/wiki/Documentation)
* [Windows Vagrant Boxes](https://app.vagrantup.com/boxes/search)

---
