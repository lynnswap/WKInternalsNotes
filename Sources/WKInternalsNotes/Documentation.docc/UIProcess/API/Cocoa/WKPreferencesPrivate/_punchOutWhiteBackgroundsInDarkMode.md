# ``WKInternalsNotes/WKPreferences/_punchOutWhiteBackgroundsInDarkMode``

Punch Out White Backgrounds In Dark Mode を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPunchOutWhiteBackgroundsInDarkMode:) BOOL _punchOutWhiteBackgroundsInDarkMode WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_punchOutWhiteBackgroundsInDarkMode = YES`: Punch Out White Backgrounds In Dark Mode を有効化する。
- `_punchOutWhiteBackgroundsInDarkMode = NO`: Punch Out White Backgrounds In Dark Mode を無効化する。
- Implementation: [`Document.cpp#L9942`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L9942) の `Color::isWhiteColor` が `punchOutWhiteBackgroundsInDarkMode()` を参照する。

## Details
- WebPreferences key: `PunchOutWhiteBackgroundsInDarkMode`

## References
- [`WKPreferencesPrivate.h#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L158)
- [`WKPreferences.mm#L868`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L868)
- [`Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`UnifiedWebPreferences.yaml#L6231`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6231) (key: `PunchOutWhiteBackgroundsInDarkMode`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
