# ``WKInternalsNotes/WKWebpagePreferences/_customHeaderFields``

カスタムヘッダフィールドの一覧を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setCustomHeaderFields:) NSArray<_WKCustomHeaderFields *> *_customHeaderFields;
```

## Default Value
初期値は `WebsitePolicies::customHeaderFields()` の状態に依存する。

## Discussion
getter は `customHeaderFields()` を `_WKCustomHeaderFields` の配列にラップして返す。setter は配列を `WebCore::CustomHeaderFields` の vector に変換して設定する。

## References
- [`WKWebpagePreferencesPrivate.h#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L102)
- [`WKWebpagePreferences.mm#L396`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L396)
- [`WKWebpagePreferences.mm#L403`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L403)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
