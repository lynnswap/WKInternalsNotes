# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_portsForUpgradingInsecureSchemeForTesting``

insecure→secure upgrade のテスト用ポート

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPortsForUpgradingInsecureSchemeForTesting:) NSArray<NSNumber *> *_portsForUpgradingInsecureSchemeForTesting WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: port の特別扱いはなく、通常の https upgrade が行われる。
- `_portsForUpgradingInsecureSchemeForTesting = [from, to]` を設定すると: https upgrade の際に、port が `from` の URL を `to` へ差し替える（テスト用）。
- `nil` に戻すと: 差し替えを無効化する。

## Details
- `[from, to]` の2要素

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L112`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L112)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L845`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L845)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
