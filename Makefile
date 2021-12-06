.PHONY: all

all:
	@{ \
	cd unit-converter-frontend ;\
	ng build --prod --build-optimizer --baseHref="/static/" ;\
	cd .. ;\
	cp unit-converter-frontend/dist/unit-converter-frontend/*.js unit-converter-backend/swagger_server/static ;\
	cp unit-converter-frontend/dist/unit-converter-frontend/*.css unit-converter-backend/swagger_server/static ;\
	cp unit-converter-frontend/dist/unit-converter-frontend/*.ico unit-converter-backend/swagger_server/static ;\
	cp unit-converter-frontend/dist/unit-converter-frontend/*.txd unit-converter-backend/swagger_server/static ;\
	cp unit-converter-frontend/dist/unit-converter-frontend/*.html unit-converter-backend/swagger_server/templates ;\
	cd unit-converter-backend ;\
	make ;\
	}
