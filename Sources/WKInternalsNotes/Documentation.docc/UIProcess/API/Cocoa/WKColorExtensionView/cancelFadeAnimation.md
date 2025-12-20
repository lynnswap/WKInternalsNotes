# ``WKInternalsNotes/WKColorExtensionView/cancelFadeAnimation()``

フェードアニメーションをキャンセルする。

## Objective-C Declaration
```objective-c
- (void)cancelFadeAnimation;
```

## Discussion
`_targetColor` が未設定の場合は何もしない。アニメーションを削除し、背景色を `_targetColor` に戻したうえで `hidden` を `_isVisible` の状態に合わせる。

## References
- [`WKColorExtensionView.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.h#L49)
- [`WKColorExtensionView.mm#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L116)
- [`WKColorExtensionView.mm#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L118)
- [`WKColorExtensionView.mm#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L122)
- [`WKColorExtensionView.mm#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L123)
- [`WKColorExtensionView.mm#L124`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.mm#L124)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
