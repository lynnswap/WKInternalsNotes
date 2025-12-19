# ``WKInternalsNotes/WKWebpagePreferences/_contentBlockersEnabled``

コンテンツブロッカーの既定有効/無効を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setContentBlockersEnabled:) BOOL _contentBlockersEnabled;
```

## Default Value
初期値は `API::WebsitePolicies` の content extension enablement の既定値に依存する。

## Discussion
setter は default enablement を Enabled/Disabled に切り替え、例外は空で設定する。getter は例外を無視して既定値のみを返す。

## References
- [`WKWebpagePreferencesPrivate.h#L98`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L98)
- [`WKWebpagePreferences.mm#L201`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L201)
- [`WKWebpagePreferences.mm#L207`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L207)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
