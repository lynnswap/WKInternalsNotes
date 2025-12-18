# ``WKInternalsNotes/WKPreferences/_showsToolTipOverTruncatedText``

Shows Tool Tip Over Truncated Text を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShowsToolTipOverTruncatedText:) BOOL _showsToolTipOverTruncatedText WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_showsToolTipOverTruncatedText = YES`: Shows Tool Tip Over Truncated Text を有効化する。
- `_showsToolTipOverTruncatedText = NO`: Shows Tool Tip Over Truncated Text を無効化する。
- Implementation: [`Chrome.cpp#L348`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/Chrome.cpp#L348) の `Chrome::getToolTip` が `showsToolTipOverTruncatedText()` を参照する。

## Details
- WebPreferences key: `ShowsToolTipOverTruncatedText`

## References
- [`WKPreferencesPrivate.h#L235`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L235)
- [`WKPreferences.mm#L1289`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1289)
- [`Chrome.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/Chrome.cpp)
- [`UnifiedWebPreferences.yaml#L7371`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7371) (key: `ShowsToolTipOverTruncatedText`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
