
ALL_SKILLS = {
    
    # ========================================
    # PROGRAMMING LANGUAGES
    # ========================================
    
        "python": {"weight": 5, "aliases": ["py", "python3", "python2"]},
        "java": {"weight": 5, "aliases": ["java8", "java11", "java17", "java21"]},
        "javascript": {"weight": 5, "aliases": ["js", "es6", "es2015", "ecmascript"]},
        "typescript": {"weight": 4, "aliases": ["ts"]},
        "c++": {"weight": 4, "aliases": ["cpp", "cplusplus", "c plus plus"]},
        "c": {"weight": 3, "aliases": ["clang"]},
        "c#": {"weight": 4, "aliases": ["csharp", "c sharp", "dotnet"]},
        "go": {"weight": 4, "aliases": ["golang"]},
        "rust": {"weight": 3, "aliases": []},
        "php": {"weight": 3, "aliases": ["php7", "php8"]},
        "ruby": {"weight": 3, "aliases": ["ruby on rails", "ror"]},
        "swift": {"weight": 4, "aliases": ["swiftui"]},
        "kotlin": {"weight": 4, "aliases": []},
        "scala": {"weight": 3, "aliases": []},
        "r": {"weight": 3, "aliases": ["rlang"]},
        "matlab": {"weight": 2, "aliases": []},
        "perl": {"weight": 2, "aliases": []},
        "dart": {"weight": 3, "aliases": []},
        "elixir": {"weight": 2, "aliases": []},
        "haskell": {"weight": 2, "aliases": []},
        "lua": {"weight": 2, "aliases": []},
        "shell": {"weight": 3, "aliases": ["bash", "zsh", "sh", "shell scripting"]},
        "powershell": {"weight": 2, "aliases": []},
        "sql": {"weight": 5, "aliases": ["structured query language", "t-sql", "pl/sql"]},
    
    
    # ========================================
    # FRONTEND FRAMEWORKS & LIBRARIES
    # ========================================
    
        "react": {"weight": 5, "aliases": ["reactjs", "react.js", "react js"]},
        "angular": {"weight": 4, "aliases": ["angularjs", "angular2", "angular 2+"]},
        "vue": {"weight": 4, "aliases": ["vuejs", "vue.js", "vue js"]},
        "svelte": {"weight": 3, "aliases": ["sveltejs"]},
        "nextjs": {"weight": 4, "aliases": ["next.js", "next js", "next"]},
        "nuxtjs": {"weight": 3, "aliases": ["nuxt.js", "nuxt"]},
        "gatsby": {"weight": 2, "aliases": ["gatsbyjs"]},
        "remix": {"weight": 3, "aliases": []},
        "jquery": {"weight": 2, "aliases": []},
        "bootstrap": {"weight": 3, "aliases": ["bootstrap4", "bootstrap5"]},
        "tailwindcss": {"weight": 4, "aliases": ["tailwind"]},
        "materialui": {"weight": 3, "aliases": ["mui", "material-ui", "material ui"]},
        "antdesign": {"weight": 2, "aliases": ["ant design", "antd"]},
        "chakraui": {"weight": 2, "aliases": ["chakra ui", "chakra"]},
        "redux": {"weight": 4, "aliases": ["redux toolkit", "rtk"]},
        "mobx": {"weight": 2, "aliases": []},
        "recoil": {"weight": 2, "aliases": []},
        "zustand": {"weight": 2, "aliases": []},
        "sass": {"weight": 3, "aliases": ["scss"]},
        "less": {"weight": 2, "aliases": []},
        "webpack": {"weight": 3, "aliases": []},
        "vite": {"weight": 3, "aliases": []},
        "parcel": {"weight": 2, "aliases": []},
        "babel": {"weight": 3, "aliases": []},
        "html": {"weight": 4, "aliases": ["html5"]},
        "css": {"weight": 4, "aliases": ["css3"]},
        "webassembly": {"weight": 2, "aliases": ["wasm"]},
    
    
    # ========================================
    # BACKEND FRAMEWORKS
    # ========================================
    
        "nodejs": {"weight": 5, "aliases": ["node.js", "node js", "node"]},
        "express": {"weight": 5, "aliases": ["expressjs", "express.js"]},
        "nestjs": {"weight": 4, "aliases": ["nest.js", "nest"]},
        "fastify": {"weight": 3, "aliases": []},
        "koa": {"weight": 2, "aliases": ["koajs"]},
        "django": {"weight": 5, "aliases": []},
        "flask": {"weight": 4, "aliases": []},
        "fastapi": {"weight": 4, "aliases": ["fast api"]},
        "springboot": {"weight": 5, "aliases": ["spring boot", "spring"]},
        "laravel": {"weight": 4, "aliases": []},
        "symfony": {"weight": 2, "aliases": []},
        "rubyonrails": {"weight": 3, "aliases": ["rails", "ror"]},
        "aspnet": {"weight": 4, "aliases": ["asp.net", "asp net core", ".net core"]},
        "gin": {"weight": 3, "aliases": []},
        "echo": {"weight": 2, "aliases": []},
        "fiber": {"weight": 2, "aliases": []},
        "phoenix": {"weight": 2, "aliases": []},
        "actix": {"weight": 2, "aliases": ["actix-web"]},
    
    
    # ========================================
    # MOBILE DEVELOPMENT
    # ========================================
    
        "reactnative": {"weight": 5, "aliases": ["react native", "react-native", "rn"]},
        "flutter": {"weight": 5, "aliases": []},
        "swift": {"weight": 4, "aliases": ["swiftui"]},
        "kotlin": {"weight": 4, "aliases": []},
        "ios": {"weight": 4, "aliases": ["ios development"]},
        "android": {"weight": 4, "aliases": ["android development"]},
        "xamarin": {"weight": 2, "aliases": []},
        "ionic": {"weight": 2, "aliases": []},
        "cordova": {"weight": 2, "aliases": []},
        "jetpackcompose": {"weight": 3, "aliases": ["jetpack compose"]},
    
    
    # ========================================
    # DATABASES
    # ========================================
    
        "mysql": {"weight": 4, "aliases": []},
        "postgresql": {"weight": 5, "aliases": ["postgres", "psql"]},
        "mongodb": {"weight": 5, "aliases": ["mongo"]},
        "sqlite": {"weight": 2, "aliases": []},
        "redis": {"weight": 4, "aliases": []},
        "cassandra": {"weight": 3, "aliases": []},
        "dynamodb": {"weight": 3, "aliases": []},
        "firebase": {"weight": 4, "aliases": ["firestore"]},
        "supabase": {"weight": 3, "aliases": []},
        "elasticsearch": {"weight": 4, "aliases": ["elastic search"]},
        "neo4j": {"weight": 2, "aliases": []},
        "influxdb": {"weight": 2, "aliases": []},
        "timescaledb": {"weight": 2, "aliases": []},
        "cockroachdb": {"weight": 2, "aliases": []},
        "mariadb": {"weight": 3, "aliases": []},
        "oracle": {"weight": 3, "aliases": ["oracle db"]},
        "mssql": {"weight": 3, "aliases": ["sql server", "microsoft sql server"]},
        "nosql": {"weight": 3, "aliases": []},
    
    
    # ========================================
    # CLOUD PLATFORMS
    # ========================================
    
        "aws": {"weight": 5, "aliases": ["amazon web services"]},
        "azure": {"weight": 4, "aliases": ["microsoft azure"]},
        "gcp": {"weight": 4, "aliases": ["google cloud platform", "google cloud"]},
        "heroku": {"weight": 2, "aliases": []},
        "digitalocean": {"weight": 2, "aliases": []},
        "vercel": {"weight": 3, "aliases": []},
        "netlify": {"weight": 2, "aliases": []},
        "cloudflare": {"weight": 3, "aliases": []},
        "linode": {"weight": 2, "aliases": []},
        "railway": {"weight": 2, "aliases": []},
        "render": {"weight": 2, "aliases": []},

    
    # ========================================
    # AWS SERVICES
    # ========================================
    
        "ec2": {"weight": 4, "aliases": ["elastic compute cloud"]},
        "s3": {"weight": 4, "aliases": ["simple storage service"]},
        "lambda": {"weight": 4, "aliases": ["aws lambda"]},
        "rds": {"weight": 3, "aliases": ["relational database service"]},
        "dynamodb": {"weight": 3, "aliases": []},
        "cloudformation": {"weight": 3, "aliases": []},
        "ecs": {"weight": 3, "aliases": ["elastic container service"]},
        "eks": {"weight": 3, "aliases": ["elastic kubernetes service"]},
        "cloudwatch": {"weight": 3, "aliases": []},
        "sns": {"weight": 2, "aliases": ["simple notification service"]},
        "sqs": {"weight": 3, "aliases": ["simple queue service"]},
        "apigateway": {"weight": 3, "aliases": ["api gateway"]},
        "cognito": {"weight": 2, "aliases": []},
        "amplify": {"weight": 2, "aliases": []},
    
    
    # ========================================
    # DEVOPS & CI/CD
    # ========================================
    
        "docker": {"weight": 5, "aliases": []},
        "kubernetes": {"weight": 5, "aliases": ["k8s"]},
        "jenkins": {"weight": 4, "aliases": []},
        "githubactions": {"weight": 4, "aliases": ["github actions"]},
        "gitlabci": {"weight": 3, "aliases": ["gitlab ci", "gitlab ci/cd"]},
        "circleci": {"weight": 3, "aliases": ["circle ci"]},
        "travis": {"weight": 2, "aliases": ["travis ci", "travisci"]},
        "terraform": {"weight": 4, "aliases": []},
        "ansible": {"weight": 3, "aliases": []},
        "puppet": {"weight": 2, "aliases": []},
        "chef": {"weight": 2, "aliases": []},
        "vagrant": {"weight": 2, "aliases": []},
        "helm": {"weight": 3, "aliases": []},
        "argocd": {"weight": 3, "aliases": ["argo cd"]},
        "nginx": {"weight": 4, "aliases": []},
        "apache": {"weight": 3, "aliases": []},
        "cicd": {"weight": 4, "aliases": ["ci/cd", "continuous integration"]},
    
    
    # ========================================
    # VERSION CONTROL
    # ========================================
    
        "git": {"weight": 5, "aliases": []},
        "github": {"weight": 4, "aliases": []},
        "gitlab": {"weight": 3, "aliases": []},
        "bitbucket": {"weight": 3, "aliases": []},
        "svn": {"weight": 2, "aliases": ["subversion"]},
        "mercurial": {"weight": 1, "aliases": []},
    
    
    # ========================================
    # DATA SCIENCE & ML
    # ========================================
    
        "machinelearning": {"weight": 5, "aliases": ["machine learning", "ml"]},
        "deeplearning": {"weight": 5, "aliases": ["deep learning", "dl"]},
        "nlp": {"weight": 4, "aliases": ["natural language processing"]},
        "computervision": {"weight": 4, "aliases": ["computer vision", "cv"]},
        "tensorflow": {"weight": 4, "aliases": ["tf"]},
        "pytorch": {"weight": 5, "aliases": []},
        "keras": {"weight": 3, "aliases": []},
        "scikitlearn": {"weight": 4, "aliases": ["scikit-learn", "sklearn"]},
        "pandas": {"weight": 5, "aliases": []},
        "numpy": {"weight": 5, "aliases": []},
        "scipy": {"weight": 3, "aliases": []},
        "matplotlib": {"weight": 3, "aliases": []},
        "seaborn": {"weight": 3, "aliases": []},
        "plotly": {"weight": 3, "aliases": []},
        "jupyter": {"weight": 4, "aliases": ["jupyter notebook", "jupyterlab"]},
        "opencv": {"weight": 3, "aliases": ["cv2"]},
        "spacy": {"weight": 3, "aliases": []},
        "nltk": {"weight": 3, "aliases": []},
        "huggingface": {"weight": 4, "aliases": ["hugging face", "transformers"]},
        "langchain": {"weight": 3, "aliases": []},
        "llm": {"weight": 4, "aliases": ["large language model", "large language models"]},
        "gpt": {"weight": 3, "aliases": []},
        "bert": {"weight": 3, "aliases": []},
    
    
    # ========================================
    # BIG DATA & ANALYTICS
    # ========================================
    
        "spark": {"weight": 4, "aliases": ["apache spark", "pyspark"]},
        "hadoop": {"weight": 3, "aliases": ["apache hadoop"]},
        "kafka": {"weight": 4, "aliases": ["apache kafka"]},
        "airflow": {"weight": 4, "aliases": ["apache airflow"]},
        "flink": {"weight": 2, "aliases": ["apache flink"]},
        "hive": {"weight": 2, "aliases": []},
        "presto": {"weight": 2, "aliases": []},
        "snowflake": {"weight": 3, "aliases": []},
        "databricks": {"weight": 3, "aliases": []},
        "redshift": {"weight": 3, "aliases": ["amazon redshift"]},
        "bigquery": {"weight": 3, "aliases": ["google bigquery"]},
        "tableau": {"weight": 3, "aliases": []},
        "powerbi": {"weight": 4, "aliases": ["power bi"]},
        "looker": {"weight": 2, "aliases": []},
        "dbt": {"weight": 3, "aliases": []},
    
    
    # ========================================
    # TESTING
    # ========================================
    
        "jest": {"weight": 4, "aliases": []},
        "mocha": {"weight": 3, "aliases": []},
        "chai": {"weight": 2, "aliases": []},
        "cypress": {"weight": 4, "aliases": []},
        "playwright": {"weight": 4, "aliases": []},
        "selenium": {"weight": 4, "aliases": []},
        "junit": {"weight": 3, "aliases": []},
        "testng": {"weight": 2, "aliases": []},
        "pytest": {"weight": 4, "aliases": []},
        "unittest": {"weight": 3, "aliases": []},
        "tdd": {"weight": 3, "aliases": ["test driven development"]},
        "bdd": {"weight": 2, "aliases": ["behavior driven development"]},
        "cucumber": {"weight": 2, "aliases": []},
        "postman": {"weight": 4, "aliases": []},
        "insomnia": {"weight": 2, "aliases": []},
        "jmeter": {"weight": 2, "aliases": []},
        "k6": {"weight": 2, "aliases": []},
    
    
    # ========================================
    # API & PROTOCOLS
    # ========================================
    
        "rest": {"weight": 5, "aliases": ["restful", "rest api", "restful api"]},
        "graphql": {"weight": 4, "aliases": []},
        "grpc": {"weight": 3, "aliases": []},
        "soap": {"weight": 2, "aliases": []},
        "websocket": {"weight": 3, "aliases": ["websockets"]},
        "webhook": {"weight": 3, "aliases": ["webhooks"]},
        "openapi": {"weight": 3, "aliases": ["swagger"]},
        "jsonapi": {"weight": 2, "aliases": ["json api"]},
    
    
    # ========================================
    # MESSAGE QUEUES
    # ========================================
    
        "rabbitmq": {"weight": 4, "aliases": ["rabbit mq"]},
        "kafka": {"weight": 4, "aliases": ["apache kafka"]},
        "redis": {"weight": 4, "aliases": ["redis queue"]},
        "sqs": {"weight": 3, "aliases": ["amazon sqs"]},
        "celery": {"weight": 3, "aliases": []},
        "bull": {"weight": 2, "aliases": ["bullmq"]},
        "activemq": {"weight": 2, "aliases": []},
    
    
    # ========================================
    # MONITORING & OBSERVABILITY
    # ========================================
    
        "prometheus": {"weight": 4, "aliases": []},
        "grafana": {"weight": 4, "aliases": []},
        "elk": {"weight": 4, "aliases": ["elasticsearch logstash kibana", "elk stack"]},
        "datadog": {"weight": 3, "aliases": []},
        "newrelic": {"weight": 3, "aliases": ["new relic"]},
        "sentry": {"weight": 3, "aliases": []},
        "splunk": {"weight": 2, "aliases": []},
        "dynatrace": {"weight": 2, "aliases": []},
        "appinsights": {"weight": 2, "aliases": ["application insights"]},
        "cloudwatch": {"weight": 3, "aliases": []},
    
    
    # ========================================
    # SECURITY
    # ========================================
    
        "oauth": {"weight": 4, "aliases": ["oauth2", "oauth 2.0"]},
        "jwt": {"weight": 4, "aliases": ["json web token"]},
        "ssl": {"weight": 3, "aliases": ["tls", "https"]},
        "encryption": {"weight": 3, "aliases": []},
        "authentication": {"weight": 4, "aliases": ["auth"]},
        "authorization": {"weight": 4, "aliases": []},
        "owasp": {"weight": 3, "aliases": []},
        "penetrationtesting": {"weight": 3, "aliases": ["penetration testing", "pen testing"]},
        "iam": {"weight": 3, "aliases": ["identity and access management"]},
        "sso": {"weight": 3, "aliases": ["single sign-on"]},
        "saml": {"weight": 2, "aliases": []},
    
    
    # ========================================
    # BLOCKCHAIN & WEB3
    # ========================================
    
        "solidity": {"weight": 3, "aliases": []},
        "ethereum": {"weight": 3, "aliases": []},
        "smartcontracts": {"weight": 3, "aliases": ["smart contracts"]},
        "web3": {"weight": 3, "aliases": ["web3.js"]},
        "hardhat": {"weight": 2, "aliases": []},
        "truffle": {"weight": 2, "aliases": []},
        "ipfs": {"weight": 2, "aliases": []},
        "nft": {"weight": 2, "aliases": ["nfts"]},
        "defi": {"weight": 2, "aliases": []},
    
    
    # ========================================
    # GAME DEVELOPMENT
    # ========================================
    
        "unity": {"weight": 4, "aliases": []},
        "unreal": {"weight": 4, "aliases": ["unreal engine"]},
        "godot": {"weight": 2, "aliases": []},
        "phaser": {"weight": 2, "aliases": []},
        "webgl": {"weight": 2, "aliases": []},
        "threejs": {"weight": 3, "aliases": ["three.js"]},
        "babylonjs": {"weight": 2, "aliases": []},
    
    
    # ========================================
    # DESIGN & UI/UX
    # ========================================
    
        "figma": {"weight": 4, "aliases": []},
        "adobexd": {"weight": 3, "aliases": ["adobe xd", "xd"]},
        "sketch": {"weight": 3, "aliases": []},
        "photoshop": {"weight": 3, "aliases": ["adobe photoshop", "ps"]},
        "illustrator": {"weight": 2, "aliases": ["adobe illustrator", "ai"]},
        "aftereffects": {"weight": 2, "aliases": ["after effects"]},
        "invision": {"weight": 2, "aliases": []},
        "zeplin": {"weight": 2, "aliases": []},
        "wireframing": {"weight": 3, "aliases": []},
        "prototyping": {"weight": 3, "aliases": []},
        "userresearch": {"weight": 3, "aliases": ["user research"]},
        "uxdesign": {"weight": 4, "aliases": ["ux design", "user experience"]},
        "uidesign": {"weight": 4, "aliases": ["ui design", "user interface"]},
    
    
    # ========================================
    # CONCEPTS & PRINCIPLES
    # ========================================
    
        "datastructures": {"weight": 5, "aliases": ["data structures", "dsa"]},
        "algorithms": {"weight": 5, "aliases": []},
        "oops": {"weight": 5, "aliases": ["oop", "object oriented programming"]},
        "systemdesign": {"weight": 5, "aliases": ["system design"]},
        "microservices": {"weight": 4, "aliases": ["micro services"]},
        "restfulapi": {"weight": 4, "aliases": ["restful api", "rest api"]},
        "designpatterns": {"weight": 4, "aliases": ["design patterns"]},
        "solid": {"weight": 3, "aliases": ["solid principles"]},
        "dry": {"weight": 2, "aliases": ["don't repeat yourself"]},
        "agile": {"weight": 4, "aliases": ["agile methodology"]},
        "scrum": {"weight": 4, "aliases": []},
        "kanban": {"weight": 3, "aliases": []},
        "tdd": {"weight": 3, "aliases": ["test driven development"]},
        "multithreading": {"weight": 3, "aliases": ["multi threading", "concurrency"]},
        "asynchronous": {"weight": 3, "aliases": ["async", "async programming"]},
        "eventdriven": {"weight": 3, "aliases": ["event driven", "event-driven architecture"]},
        "serverless": {"weight": 3, "aliases": []},
        "distributed systems": {"weight": 4, "aliases": ["distributedsystems"]},
    
    
    # ========================================
    # PROJECT MANAGEMENT
    # ========================================
    
        "jira": {"weight": 4, "aliases": []},
        "trello": {"weight": 3, "aliases": []},
        "asana": {"weight": 3, "aliases": []},
        "confluence": {"weight": 3, "aliases": []},
        "notion": {"weight": 3, "aliases": []},
        "monday": {"weight": 2, "aliases": ["monday.com"]},
        "clickup": {"weight": 2, "aliases": []},
        "linear": {"weight": 2, "aliases": []},
    
    
    # ========================================
    # OPERATING SYSTEMS
    # ========================================
    
        "linux": {"weight": 4, "aliases": []},
        "ubuntu": {"weight": 3, "aliases": []},
        "centos": {"weight": 2, "aliases": []},
        "debian": {"weight": 2, "aliases": []},
        "redhat": {"weight": 2, "aliases": ["rhel"]},
        "macos": {"weight": 2, "aliases": ["mac os", "osx"]},
        "windows": {"weight": 3, "aliases": []},
        "unix": {"weight": 3, "aliases": []},
    
    
    # ========================================
    # NETWORKING
    # ========================================
    
        "tcp/ip": {"weight": 3, "aliases": ["tcpip", "tcp ip"]},
        "http": {"weight": 4, "aliases": ["https"]},
        "dns": {"weight": 3, "aliases": []},
        "loadbalancing": {"weight": 3, "aliases": ["load balancing"]},
        "cdn": {"weight": 3, "aliases": ["content delivery network"]},
        "vpn": {"weight": 2, "aliases": []},
        "firewall": {"weight": 2, "aliases": []},
    
    
    # ========================================
    # EMBEDDED & IOT
    # ========================================
   
        "embedded": {"weight": 3, "aliases": ["embedded systems"]},
        "iot": {"weight": 3, "aliases": ["internet of things"]},
        "arduino": {"weight": 2, "aliases": []},
        "raspberrypi": {"weight": 2, "aliases": ["raspberry pi"]},
        "mqtt": {"weight": 2, "aliases": []},
        "rtos": {"weight": 2, "aliases": ["real time operating system"]},
 
    
    # ========================================
    # SOFT SKILLS
    # ========================================
   
        "problemsolving": {"weight": 2, "aliases": ["problem solving"]},
        "communication": {"weight": 2, "aliases": []},
        "leadership": {"weight": 2, "aliases": []},
        "teamwork": {"weight": 2, "aliases": ["collaboration"]},
        "criticalthinking": {"weight": 2, "aliases": ["critical thinking"]},
        "timemanagement": {"weight": 1, "aliases": ["time management"]},
        "adaptability": {"weight": 1, "aliases": []},
        "creativity": {"weight": 1, "aliases": []},
        "analytical": {"weight": 2, "aliases": ["analytical skills"]},

    
    # ========================================
    # ADDITIONAL TOOLS & PLATFORMS
    # ========================================
 
        "vscode": {"weight": 3, "aliases": ["visual studio code"]},
        "intellij": {"weight": 3, "aliases": ["intellij idea"]},
        "eclipse": {"weight": 2, "aliases": []},
        "vim": {"weight": 2, "aliases": []},
        "emacs": {"weight": 1, "aliases": []},
        "slack": {"weight": 3, "aliases": []},
        "teams": {"weight": 2, "aliases": ["microsoft teams"]},
        "zoom": {"weight": 2, "aliases": []},
        "discord": {"weight": 2, "aliases": []},
    
}


