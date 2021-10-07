import QtQuick 2.0

Item {
        property string sfitext // Declare properties here
        property string nameText
        property string clsText
        property string flagText
        property string ownrText
        property string deptText
        property string dateText
        property string hourText
        property string estText
        property string statText
        property string respNameText

        id: base
        width:30
        height: 100

    Rectangle {
        id: background
        // color: "#bdc2e8"
        radius: height/2
        border.width: 2
        anchors.fill: parent
        // anchors.rightMargin: 5
        anchors.bottomMargin: 2.5
        // anchors.leftMargin: 5
        anchors.topMargin: 2.5

        
        Text{
            id: sfi
            anchors {
                top: parent.top
                left: parent.left
            }
            width: parent.height*3/4
            height: parent.height
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter

            text: sfitext // And use them here

        }
        
        
        Text {
            id: name
            width: parent.width - sfi.width - stat.width
            height: parent.height/2
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            wrapMode: Text.WordWrap
            font{
                pixelSize: base.height/5
                weight: Text.DemiBold
                family: 'Effra'
            }
            anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
            }
            text: nameText // And use them here
        }
        
        
        Text{
            id: cls
            width: (parent.width - parent.height)/6
            y: parent.height*3/4
            anchors {
                left: sfi.right
            }
            text: "C: " + clsText // And use them here
        }
        
        
        Text{
            id: flag
            width: (parent.width - parent.height)/6
            y: parent.height*3/4
            anchors {
                left: cls.right
                }
            text: "F: " + flagText // And use them here
        }
        
        
        Text {
            width: (parent.width - parent.height)/6
            y: parent.height*3/4
            anchors {
                left: flag.right
            }
            text: "O: " + ownrText // And use them here
        }
        
        
        Text{
            id: dept
            width: (parent.width - parent.height)/2
            height: parent.height/4
            anchors {
                top: parent.verticalCenter
                left: sfi.right
            }
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            text: deptText // And use them here
        }
        
        Text{
            //advance: size
            //baseUrl: url
            //bottomPadding: real
            //clip: bool
            //color: color
            //contentHeight: real
            //contentWidth: real
            //effectiveHorizontalAlignment: enumeration
            //elide: enumeration
            //font.bold: bool
            //font.capitalization: enumeration
            //font.family: string
            //font.hintingPreference: enumeration
            //font.italic: bool
            //font.kerning: bool
            //font.letterSpacing: real
            //font.pixelSize: int
            //font.pointSize: real
            //font.preferShaping: bool
            //font.strikeout: bool
            //font.styleName: string
            //font.underline: bool
            //font.weight: enumeration
            //font.wordSpacing: real
            //fontInfo.bold: bool
            //fontInfo.family: string
            //fontInfo.italic: bool
            //fontInfo.pixelSize: string
            //fontInfo.pointSize: real
            //fontInfo.styleName: string
            //fontInfo.weight: int
            //fontSizeMode: enumeration
            //horizontalAlignment: enumeration
            //hoveredLink: string
            //leftPadding: real
            //lineCount: int
            //lineHeight: real
            //lineHeightMode: enumeration
            //linkColor: color
            //maximumLineCount: int
            //minimumPixelSize: int
            //minimumPointSize: int
            //padding: real
            //renderType: enumeration
            //rightPadding: real
            //style: enumeration
            //styleColor: color
            //text: string
            //textFormat: enumeration
            //topPadding: real
            //truncated: bool
            //verticalAlignment: enumeration
            //wrapMode: enumeration
            //doLayout()(obsolete)
            //forceLayout()
            //lineLaidOut(objectline)
            //linkActivated(stringlink)
            //linkAt(realx,realy)
            //linkHovered(stringlink)
            //
            //
            //activeFocus: bool
            //activeFocusOnTab: bool
            //anchors.alignWhenCentered: bool
            //anchors.baseline: AnchorLine
            //anchors.baselineOffset: real
            //anchors.bottom: AnchorLine
            //anchors.bottomMargin: real
            //anchors.centerIn: Item
            //anchors.fill: Item
            //anchors.horizontalCenter: AnchorLine
            //anchors.horizontalCenterOffset: real
            //anchors.left: AnchorLine
            //anchors.leftMargin: real
            //anchors.margins: real
            //anchors.right: AnchorLine
            //anchors.rightMargin: real
            //anchors.top: AnchorLine
            //anchors.topMargin: real
            //anchors.verticalCenter: AnchorLine
            //anchors.verticalCenterOffset: real
            //antialiasing: bool
            //baselineOffset: int
            //children: list<Item>
            //childrenRect.height: real
            //childrenRect.width: real
            //childrenRect.x: real
            //childrenRect.y: real
            //clip: bool
            //containmentMask: QObject*
            //data: list<Object>
            //enabled: bool
            //focus: bool
            //height: real
            //implicitHeight: real
            //implicitWidth: real
            //layer.effect: Component
            //layer.enabled: bool
            //layer.format: enumeration
            //layer.mipmap: bool
            //layer.samplerName: string
            //layer.samples: enumeration
            //layer.smooth: bool
            //layer.sourceRect: rect
            //layer.textureMirroring: enumeration
            //layer.textureSize: size
            //layer.wrapMode: enumeration
            //opacity: real
            //parent: Item
            //resources: list<Object>
            //rotation: real
            //scale: real
            //smooth: bool
            //state: string
            //states: list<State>
            //transform: list<Transform>
            //transformOrigin: enumeration
            //transitions: list<Transition>
            //visible: bool
            //visibleChildren: list<Item>
            //width: real
            //x: real
            //y: real
            //z: real
            //childAt(realx,realy)
            //forceActiveFocus()
            //forceActiveFocus(Qt: : FocusReasonreason)
            //nextItemInFocusChain(boolforward)
            //objectName: string
        }
        
        Text{
            id: date
            x: parent.width/2
            y: parent.height/2
            width: (parent.width-parent.height)/2
            height: parent.height/4
            anchors {
                verticalCenter : dept.verticalCenter
            }
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter

            text: dateText // And use them here
        }
        
        
        Text{
            id: startHour
            height: parent.height/4
            width: date.width/2
            anchors {
                left: date.left
                verticalCenter: flag.verticalCenter
            }
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            text: hourText // And use them here
        }
        
        Text{
            height: parent.height/4
            width: date.width/2
            anchors {
                verticalCenter: startHour.verticalCenter
                left: startHour.right
            }
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            
            text: estText // And use them here
        }
        
        Text{
            id: stat
            height: parent.height
            width: parent.height*3/4
            anchors {
                right: parent.right
                top: parent.top    
            }
            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
            text: statText // And use them here
        }
        
    }

    onStatTextChanged: {
        if (statText == 'Not Started') {
            var gradient = passive_gradient.createObject(background)
            background.gradient = gradient;
        } else if (statText == 'Active') {
            var gradient = active_gradient.createObject(background)
            background.gradient = gradient;
        } else if (statText == 'Passed') {
            var gradient = passed_gradient.createObject(background)
            background.gradient = gradient;
        } else if (statText == 'Failed') {
            var gradient = failed_gradient.createObject(background)
            background.gradient = gradient;
        }
    }


    Component{
        id: passive_gradient
        Gradient {
            GradientStop {
                position: 0
                color: "#bdc2e8"
            }

            GradientStop {
                position: 0.01
                color: "#bdc2e8"
            }

            GradientStop {
                position: 1
                color: "#e6dee9"
            }
        }

    }

    Component{
        id: active_gradient
        Gradient {
            GradientStop {
                position: 0
                color: "#0072CE"
            }

            GradientStop {
                position: 0.01
                color: "#71a8d6"
            }

            GradientStop {
                position: 1
                color: "#e0e9f0"
            }
        }

    }

    Component{
        id: failed_gradient
        Gradient {
            GradientStop {
                position: 0
                color: "#c87979"
            }

            GradientStop {
                position: 0.01
                color: "#c87979"
            }

            GradientStop {
                position: 1
                color: "#e6dee9"
            }
        }

    }

    Component{
        id: passed_gradient
        Gradient {
            GradientStop {
                position: 0
                color: "#88cd7e"
            }

            GradientStop {
                position: 0.01
                color: "#88cd7e"
            }

            GradientStop {
                position: 1
                color: "#e6dee9"
            }
        }

    }

}