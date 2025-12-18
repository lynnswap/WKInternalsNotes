# ``WKInternalsNotes/WKView/initWithFrame(_:configurationRef:)``

page configuration を使って WKView を初期化する。

## Objective-C Declaration
```objective-c
- (id)initWithFrame:(NSRect)frame configurationRef:(WKPageConfigurationRef)configuration;
```

## Discussion
WKView では `nil` を返す。

## References
- [`WKViewPrivate.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L43)
- [`WKView.mm#L997`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L997)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
