# ``WKInternalsNotes/_WKWebAuthenticationPanelDelegate/panel(_:selectAssertionResponse:source:completionHandler:)``

複数の assertion response から選択を求める。

## Objective-C Declaration
```objective-c
- (void)panel:(_WKWebAuthenticationPanel *)panel selectAssertionResponse:(NSArray < _WKWebAuthenticationAssertionResponse *> *)responses source:(_WKWebAuthenticationSource)source completionHandler:(void (^)(_WKWebAuthenticationAssertionResponse * _Nullable))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`WebAuthenticationPanelClient::selectAssertionResponse` から呼ばれる。delegate が未設定または未実装の場合は `completionHandler(nullptr)` を呼ぶ。候補は `API::WebAuthenticationAssertionResponse` に変換して渡し、戻り値は `_WKWebAuthenticationAssertionResponse` から `_apiObject` を取り出して利用する。

## References
- [`_WKWebAuthenticationPanel.h#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L121)
- [`WebAuthenticationPanelClient.mm#L193`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WebAuthenticationPanelClient.mm#L193)
- [`WebAuthenticationPanelClient.mm#L221`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WebAuthenticationPanelClient.mm#L221)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
