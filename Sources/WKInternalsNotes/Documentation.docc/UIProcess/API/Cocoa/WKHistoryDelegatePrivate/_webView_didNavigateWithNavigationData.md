# ``WKInternalsNotes/WKHistoryDelegatePrivate/_webView(_:didNavigateWithNavigationData:)``

ナビゲーション履歴が更新されたときに呼ばれる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didNavigateWithNavigationData:(WKNavigationData *)navigationData;
```

## Discussion
NavigationState::HistoryClient が history delegate の応答可否を確認し、`API::NavigationData::create` で生成した `WKNavigationData` を渡して呼び出す。delegate が未設定または未実装の場合は何も行わない。

## References
- [`WKHistoryDelegatePrivate.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKHistoryDelegatePrivate.h#L37)
- [`NavigationState.mm#L1508`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L1508)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
