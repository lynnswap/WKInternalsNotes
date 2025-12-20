# ``WKInternalsNotes/WKColorExtensionViewDelegate/colorExtensionViewDidAppear(_:)``

カラー拡張ビューが表示された直後に呼ばれる。

## Objective-C Declaration
```objective-c
- (void)colorExtensionViewDidAppear:(WKColorExtensionView *)view;
```

## Discussion
`WKWebView` では対象がトップ側の拡張ビューかどうかを確認し、該当する場合は `prefersSolidColorHardPocket` を更新する。iOS では合わせてスクロールポケットの表示状態も更新する。

## References
- [`WKColorExtensionView.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.h#L41)
- [`WKWebView.mm#L3484`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3484)
- [`WKWebView.mm#L3486`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3486)
- [`WKWebView.mm#L3490`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3490)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
