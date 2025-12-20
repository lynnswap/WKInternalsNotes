# ``WKInternalsNotes/_WKWebAuthenticationPanel/mockConfiguration``

WebAuthn のモック設定を与える。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSDictionary *mockConfiguration;
```

## Default Value
未設定の場合は `nil`（getter 実装は確認できていない）。

## Discussion
setter は `MockWebAuthenticationConfiguration` を構築し、`userVerification` を `Yes` に固定する。`privateKeyBase64` が指定されていればローカル設定に反映し、`API::WebAuthenticationPanel` に設定する。

## References
- [`_WKWebAuthenticationPanelForTesting.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanelForTesting.h#L50)
- [`_WKWebAuthenticationPanel.mm#L1273`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1273)
- [`_WKWebAuthenticationPanel.mm#L1284`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1284)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
