TEMPLATE = aux

NAME=Swiss-keyboard-layout

OTHER_FILES = \
        arrowboard/* \
        layout/* \
        rpm/* 

arrowboard.files = arrowboard/*
arrowboard.path = /usr/share/maliit/plugins/com/jolla/arrowboard/

layout.files = layout/*
layout.path = /usr/share/maliit/plugins/com/jolla/layouts/

INSTALLS += \
        layout \
        arrowboard
