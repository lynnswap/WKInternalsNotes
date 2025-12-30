# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:openElementAtLocation:)``

指定位置で要素を開く。

## Objective-C Declaration
```objective-c
- (void)actionSheetAssistant:(WKActionSheetAssistant *)assistant openElementAtLocation:(CGPoint)location;
```

## Discussion
`_attemptSyntheticClickAtLocation:modifierFlags:` を `modifierFlags:0` で呼び、指定位置の要素を開く。

## References
- [`WKActionSheetAssistant.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L59)
- [`WKContentViewInteraction.mm#L10005`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10005)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
