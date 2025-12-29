# ``WKInternalsNotes/WKPreferenceObserver/preferenceDidChange(_:key:encodedValue:)``

設定変更を各プロセスに通知する。

## Objective-C Declaration
```objective-c
- (void)preferenceDidChange:(NSString *)domain key:(NSString *)key encodedValue:(NSString *)encodedValue;
```

## Discussion
`ENABLE(CFPREFS_DIRECT_MODE)` 時のみ有効。メインランループで `encodedValue` を `String` に変換し、GPU/Network/Web プロセスに `notifyPreferencesChanged` を送る。

## References
- [`PreferenceObserver.h#L29`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/PreferenceObserver.h#L29)
- [`PreferenceObserver.mm#L179`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/PreferenceObserver.mm#L179)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
