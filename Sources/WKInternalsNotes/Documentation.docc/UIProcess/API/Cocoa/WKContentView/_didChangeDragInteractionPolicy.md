# ``WKInternalsNotes/WKContentView/_didChangeDragInteractionPolicy()``

ドラッグインタラクションの有効状態を更新する。

## Objective-C Declaration
```objective-c
- (void)_didChangeDragInteractionPolicy;
```

## Discussion
`webView._dragInteractionPolicy` に従ってドラッグインタラクションの有効/無効を切り替える。

## References
- [`WKContentViewInteraction.h#L893`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L893)
- [`WKContentViewInteraction.mm#L10543`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10543)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
