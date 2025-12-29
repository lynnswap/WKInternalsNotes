# ``WKInternalsNotes/_WKInspectorConfiguration/applyToWebViewConfiguration(_:)``

インスペクター設定を `WKWebViewConfiguration` に適用する。

## Objective-C Declaration
```objective-c
- (void)applyToWebViewConfiguration:(WKWebViewConfiguration *)webViewConfiguration;
```

## Discussion
登録済みの URL スキームハンドラをすべて `configuration` に設定し、`processPool` と `groupIdentifier` が指定されていれば反映する。

## References
- [`_WKInspectorConfigurationInternal.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorConfigurationInternal.h#L49)
- [`_WKInspectorConfiguration.mm#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorConfiguration.mm#L78)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
