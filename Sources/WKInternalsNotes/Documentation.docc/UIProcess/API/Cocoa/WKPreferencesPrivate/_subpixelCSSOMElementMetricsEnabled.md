# ``WKInternalsNotes/WKPreferences/_subpixelCSSOMElementMetricsEnabled``

no-op（常に `NO`）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setSubpixelCSSOMElementMetricsEnabled:) BOOL _subpixelCSSOMElementMetricsEnabled WK_API_DEPRECATED("Subpixel CSSOM element metrics are no longer supported", macos(10.13.4, 10.15));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 常に `NO`。
- この API で値を設定しても: 実装が no-op のため挙動は変わらない。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L257`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L257)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1878`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1878)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
