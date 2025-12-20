# ``WKInternalsNotes/WKColorExtensionViewDelegate/colorExtensionViewWillDisappear(_:)``

カラー拡張ビューが消える直前に呼ばれる。

## Objective-C Declaration
```objective-c
- (void)colorExtensionViewWillDisappear:(WKColorExtensionView *)view;
```

## Discussion
`WKWebView` では対象がトップ側の拡張ビューかどうかを確認し、該当する場合は `prefersSolidColorHardPocket` を更新する。iOS では合わせてスクロールポケットの表示状態も更新する。

## References
- [`WKColorExtensionView.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKColorExtensionView.h#L40)
- [`WKWebView.mm#L3474`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3474)
- [`WKWebView.mm#L3476`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3476)
- [`WKWebView.mm#L3480`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3480)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
