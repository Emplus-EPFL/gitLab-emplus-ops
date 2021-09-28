# EMPLUS gitlab configuration-as-code

### Pre-requisites

- Be a member of the `emplus_epfl.gitlab` Keybase team
- Be a member of the [`emplus-git-users` group](https://groups.epfl.ch/viewgroup?groupid=S28705)
- Have ssh access to `cdhvm0024.xaas.epfl.ch`
- Have the AWS CLI installed
   - On Mac OS X: <pre>brew install awscli</pre>
   - On Ubuntu or WSL: <pre>apt update
apt install awscli</pre>
- (Optional) Install the `awscli-plugin-endpoint` plug-in:
   - On Ubuntu or WSL: <pre>sudo apt install python3-pip
sudo pip3 install awscli-plugin-endpoint
aws configure set plugins.endpoint awscli_plugin_endpoint</pre>

### Initialization part 1

Type
```
emgitsible
```

### Initialization part 2

Some tweaks have not (yet) been reduced to configuration-as-code.

#### Test access (and ensure you have an account at the same time)

1. Browse https://emplus-gitlab.epfl.ch/
1. Log in with the Tequila button

#### Set administrator privileges for yourself

You must do this using the command line (obviously this isn't feasible from the Web interface, unless you already are an administrator).

```
ssh root@cdhvm0024.xaas.epfl.ch
docker exec -it $(docker ps -q -f name=gitlabprod_v'*') gitlab-rails console
```

💡 This runs the [Rails console](https://docs.gitlab.com/ee/administration/troubleshooting/gitlab_rails_cheat_sheet.html). At the prompt,

1. Find your own user, e.g. <pre>u = User.find_by_username('MYGASPAR')</pre>⚠ be sure to replace `MYGASPAR` with your GASPAR login name.
1. [Set administrator privileges](https://forum.gitlab.com/t/how-do-i-change-my-profile-to-admin/35888) on it:<pre>u.admin = TRUE
u.save!</pre>
1. Log out of https://cdhvm0024.xaas.epfl.ch/ and back in
1. Control that you now enjoy administator privileges (the ≡ Menu at top left should now have an 🔧 Admin entry)

#### Disable username-and-password sign-in and signup

As per the [official instructions](https://docs.gitlab.com/ee/user/admin_area/settings/sign_in_restrictions.html):

1. Browse ≡ Menu → 🔧 Admin → Settings → General
1. Expand “Sign-up restrictions” and uncheck “Sign-up enabled”. Save changes with the blue button (scroll down)
1. Expand “Sign-in restrictions” and uncheck “Allow password authentication for the web interface”. Save changes with the blue button (scroll down again)
1. Log out and control that the homepage no longer shows the possibility to register by email and password. <br> 💡 People with a Tequila account and appropriate vetting can still log in, no matter whether they are within or outside of the EPFL organization (see below)

# Day-to-day operations

## Create a new account

1. If the person is not at EPFL (doesn't have a GASPAR account), have them create an account for themselves at https://guests.epfl.ch/
1. Add the person to the [`emplus-git-users` group](https://groups.epfl.ch/viewgroup?groupid=S28705)
1. Have them visit the Gitlab homepage and log in using the Tequila button
