# ``WKInternalsNotes/_WKContentWorldConfiguration/allowNodeSerialization``

`window.webkit.serializeNode` の利用可否を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL allowNodeSerialization WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Default Value
`NO`。

## Discussion
`WKContentWorld` 生成時に `AllowNodeSerialization` オプションへ反映される。

## References
- [`WKContentWorld.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorld.mm#L101)
- [`_WKContentWorldConfiguration.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentWorldConfiguration.h#L57)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
