# ``WKInternalsNotes/WKColorExtensionView/updateColor(_:)``

表示色を更新して表示状態にする。

## Objective-C Declaration
```objective-c
- (void)updateColor:(WebCore::CocoaColor *)color;
```

## Discussion
`_updateColor:visible:` を `visible:YES` で呼び出す。表示中の背景色を更新し、必要に応じてフェードアニメーションを追加する。

## References
- [`WKColorExtensionView.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.h#L47)
- [`WKColorExtensionView.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L53)
- [`WKColorExtensionView.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L55)
- [`WKColorExtensionView.mm#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L63)
- [`WKColorExtensionView.mm#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L91)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
