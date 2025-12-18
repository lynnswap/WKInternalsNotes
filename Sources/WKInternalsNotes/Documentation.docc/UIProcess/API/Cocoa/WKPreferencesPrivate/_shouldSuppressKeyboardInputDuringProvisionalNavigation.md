# ``WKInternalsNotes/WKPreferences/_shouldSuppressKeyboardInputDuringProvisionalNavigation``

Suppress Text Input From Editing During Provisional Navigation を切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShouldSuppressKeyboardInputDuringProvisionalNavigation:) BOOL _shouldSuppressKeyboardInputDuringProvisionalNavigation WK_API_AVAILABLE(macos(10.12.4), ios(10.3));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_shouldSuppressKeyboardInputDuringProvisionalNavigation = YES`: Suppress Text Input From Editing During Provisional Navigation を有効化する。
- `_shouldSuppressKeyboardInputDuringProvisionalNavigation = NO`: Suppress Text Input From Editing During Provisional Navigation を無効化する。
- Implementation: [`Source/WebCore/loader/FrameLoader.cpp#L4908`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/loader/FrameLoader.cpp#L4908) の `FrameLoader::shouldSuppressTextInputFromEditing` が `shouldSuppressTextInputFromEditingDuringProvisionalNavigation()` を参照する。

## Details
- WebPreferences key: `ShouldSuppressTextInputFromEditingDuringProvisionalNavigation`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L108`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L108)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L630`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L630)
- [`Source/WebCore/loader/FrameLoader.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/loader/FrameLoader.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7287`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7287) (key: `ShouldSuppressTextInputFromEditingDuringProvisionalNavigation`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
