# ``WKInternalsNotes/_WKContentWorldConfiguration/allowJSHandleCreation``

`window.webkit.createJSHandle` の利用可否を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL allowJSHandleCreation WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Default Value
`NO`。

## Discussion
`WKContentWorld` 生成時に `AllowJSHandleCreation` オプションへ反映される。

## References
- [`WKContentWorld.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorld.mm#L101)
- [`_WKContentWorldConfiguration.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentWorldConfiguration.h#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
