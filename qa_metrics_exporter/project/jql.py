BASER_JQL = 'project = {project} ' \
            'AND priority in (' \
            'Blocker, Critical, Major, Блокирующий, Критический, Стандартный' \
            ') ' \
            'AND created > startOfDay(-365d) ORDER BY issuekey DESC'
