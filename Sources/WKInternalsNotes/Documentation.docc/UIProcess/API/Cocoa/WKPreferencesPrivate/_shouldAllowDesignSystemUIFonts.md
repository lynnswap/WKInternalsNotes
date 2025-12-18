# ``WKInternalsNotes/WKPreferences/_shouldAllowDesignSystemUIFonts``

no-op（常に `YES`）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setShouldAllowDesignSystemUIFonts:) BOOL _shouldAllowDesignSystemUIFonts WK_API_DEPRECATED("Design system UI fonts are always enabled", macos(10.15, 15.0), ios(13.0, 18.0), visionos(1.0, 2.0));
```

## Default Value
iOS: `YES` / macOS: `YES` / visionOS: `YES`

## Discussion
- この API を使わない場合: 常に `YES`。
- この API で値を設定しても: 実装が no-op のため挙動は変わらない。

## References
- [`WKPreferencesPrivate.h#L247`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L247)
- [`WKPreferences.mm#L1800`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1800)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
