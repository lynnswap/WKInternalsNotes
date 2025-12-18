# ``WKInternalsNotes/WKPreferences/_asynchronousPluginInitializationEnabled``

no-op（常に `NO`）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAsynchronousPluginInitializationEnabled:) BOOL _asynchronousPluginInitializationEnabled WK_API_DEPRECATED("NPAPI plugins are no longer supported", macos(10.13.4, 15.0));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 常に `NO`。
- この API で値を設定しても: 実装が no-op のため挙動は変わらない。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L253`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L253)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1842`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1842)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
