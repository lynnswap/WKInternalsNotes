# ``WKInternalsNotes/WKActionSheetDelegate/hostViewForSheet()``

アクションシートを提示する親ビューを返す。

## Objective-C Declaration
```objective-c
- (UIView *)hostViewForSheet;
```

## Discussion
`WKActionSheet` のポップオーバー提示時に参照される。`WKActionSheetAssistant` では `superviewForSheet` を返す。

## References
- [`WKActionSheet.mm#L108`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L108)
- [`WKActionSheetAssistant.mm#L192`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L192)
- [`WKActionSheet.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.h#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
