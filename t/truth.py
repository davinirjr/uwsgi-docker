CONTAINERS_TRUTH = {
    u'/vassal_with_standard_socket.ini': {u'Args': [u'--ini', u'emperor://vassal_with_standard_socket.ini'],
                                          u'Config': {u'AttachStderr': True,
                                                      u'AttachStdin': True,
                                                      u'AttachStdout': True,
                                                      u'Cmd': [u'/usr/bin/uwsgi',
                                                               u'--ini',
                                                               u'emperor://vassal_with_standard_socket.ini'],
                                                      u'CpuShares': 0,
                                                      u'Cpuset': u'',
                                                      u'Domainname': u'',
                                                      u'Entrypoint': None,
                                                      u'Env': [u'UWSGI_EMPEROR_PROXY=/tmp/vassal_with_standard_socket',
                                                               u'HOME=/',
                                                               u'PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
                                                      u'ExposedPorts': {u'3031': {}, u'5000': {}},
                                                      u'Image': u'psgi001',
                                                      u'NetworkDisabled': False,
                                                      u'OnBuild': None,
                                                      u'OpenStdin': True,
                                                      u'PortSpecs': None,
                                                      u'StdinOnce': False,
                                                      u'Tty': True,
                                                      u'User': u'',
                                                      u'Volumes': None,
                                                      u'WorkingDir': u''},
                                          u'Driver': u'aufs',
                                          u'HostConfig': {u'Binds': [u'/pty/foo:/pty',
                                                                     u'/tmp/vassal_with_standard_socket.sock:/tmp/vassal_with_standard_socket'],
                                                          u'ContainerIDFile': u'',
                                                          u'Dns': [],
                                                          u'DnsSearch': None,
                                                          u'Links': None,
                                                          u'LxcConf': None,
                                                          u'NetworkMode': u'',
                                                          u'PortBindings': {u'3031': [{u'HostIp': u'0.0.0.0', u'HostPort': u'9001'}],
                                                                            u'5000': [{u'HostIp': u'127.0.0.1', u'HostPort': u'5001'}]},
                                                          u'Privileged': False,
                                                          u'PublishAllPorts': False,
                                                          u'VolumesFrom': None},
                                          u'MountLabel': u'',
                                          u'Name': u'/vassal_with_standard_socket.ini',
                                          u'NetworkSettings': {u'Bridge': u'docker0',
                                                               u'Gateway': u'172.17.42.1',
                                                               u'IPPrefixLen': 16,
                                                               u'PortMapping': None,
                                                               u'Ports': {u'3031': [{u'HostIp': u'0.0.0.0', u'HostPort': u'9001'}],
                                                                          u'5000': [{u'HostIp': u'127.0.0.1', u'HostPort': u'5001'}]}},
                                          u'Path': u'/usr/bin/uwsgi',
                                          u'ProcessLabel': u'',
                                          u'ResolvConfPath': u'/etc/resolv.conf',
                                          u'Volumes': {u'/pty': u'/pty/foo',
                                                       u'/tmp/vassal_with_standard_socket': u'/tmp/vassal_with_standard_socket.sock'},
                                          u'VolumesRW': {u'/pty': True, u'/tmp/vassal_with_standard_socket': True}},
    u'/vassal_with_docker_socket.ini': {u'Args': [u'--ini', u'emperor://vassal_with_docker_socket.ini'],
                                        u'Config': {u'AttachStderr': True,
                                                    u'AttachStdin': True,
                                                    u'AttachStdout': True,
                                                    u'Cmd': [u'/usr/bin/uwsgi',
                                                             u'--ini',
                                                             u'emperor://vassal_with_docker_socket.ini'],
                                                    u'CpuShares': 0,
                                                    u'Cpuset': u'',
                                                    u'Domainname': u'',
                                                    u'Entrypoint': None,
                                                    u'Env': [u'UWSGI_EMPEROR_PROXY=/tmp/vassal_with_docker_socket',
                                                             u'HOME=/',
                                                             u'PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
                                                    u'ExposedPorts': None,
                                                    u'Image': u'psgi001',
                                                    u'NetworkDisabled': False,
                                                    u'OnBuild': None,
                                                    u'OpenStdin': True,
                                                    u'PortSpecs': None,
                                                    u'StdinOnce': False,
                                                    u'Tty': True,
                                                    u'User': u'',
                                                    u'Volumes': None,
                                                    u'WorkingDir': u''},
                                        u'Driver': u'aufs',
                                        u'HostConfig': {u'Binds': [u'/tmp/vassal_with_docker_socket.sock:/tmp/vassal_with_docker_socket'],
                                                        u'ContainerIDFile': u'',
                                                        u'Dns': [],
                                                        u'DnsSearch': None,
                                                        u'Links': None,
                                                        u'LxcConf': None,
                                                        u'NetworkMode': u'',
                                                        u'PortBindings': {},
                                                        u'Privileged': False,
                                                        u'PublishAllPorts': False,
                                                        u'VolumesFrom': None},
                                        u'MountLabel': u'',
                                        u'Name': u'/vassal_with_docker_socket.ini',
                                        u'NetworkSettings': {u'Bridge': u'docker0',
                                                             u'Gateway': u'172.17.42.1',
                                                             u'IPPrefixLen': 16,
                                                             u'PortMapping': None,
                                                             u'Ports': {}},
                                        u'Path': u'/usr/bin/uwsgi',
                                        u'ProcessLabel': u'',
                                        u'ResolvConfPath': u'/etc/resolv.conf',
                                        u'Volumes': {u'/tmp/vassal_with_docker_socket': u'/tmp/vassal_with_docker_socket.sock'},
                                        u'VolumesRW': {u'/tmp/vassal_with_docker_socket': True}}
}
