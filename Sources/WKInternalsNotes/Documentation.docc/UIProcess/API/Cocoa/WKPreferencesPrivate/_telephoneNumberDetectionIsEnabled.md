# ``WKInternalsNotes/WKPreferencesPrivate/_telephoneNumberDetectionIsEnabled``

Telephone Number Parsing を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setTelephoneNumberDetectionIsEnabled:) BOOL _telephoneNumberDetectionIsEnabled;
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_telephoneNumberDetectionIsEnabled = YES`: Telephone Number Parsing を有効化する。
- `_telephoneNumberDetectionIsEnabled = NO`: Telephone Number Parsing を無効化する。
- Implementation: [`Source/WebCore/dom/Document.cpp#L8283`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L8283) の `Document::isTelephoneNumberParsingEnabled` が `telephoneNumberParsingEnabled()` を参照する。

## Details
- WebPreferences key: `TelephoneNumberParsingEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L72)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L246`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L246)
- [`Source/WebCore/dom/Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7813`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7813) (key: `TelephoneNumberParsingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
