.PHONY: build up down logs shell clean test help

# Variables
DC = docker-compose
APP_CONTAINER = rag-backend

help: ## Show this help
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## Build the Docker image
	$(DC) build

up: ## Start the containers in detached mode
	$(DC) up -d

down: ## Stop and remove containers
	$(DC) down

logs: ## View container logs
	$(DC) logs -f

shell: ## Open a shell inside the container
	$(DC) exec $(APP_CONTAINER) /bin/bash

test: ## Run tests inside the container
	$(DC) exec $(APP_CONTAINER) pytest

clean: ## Remove containers, networks, and images
	$(DC) down --rmi all -v --remove-orphans
