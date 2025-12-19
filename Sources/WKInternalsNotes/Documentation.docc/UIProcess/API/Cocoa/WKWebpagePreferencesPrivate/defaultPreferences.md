# ``WKInternalsNotes/WKWebpagePreferences/defaultPreferences``

既定の WKWebpagePreferences を返す。

## Objective-C Declaration
```objective-c
@property (class, nonatomic, readonly) WKWebpagePreferences *defaultPreferences;
```

## Discussion
`[[self alloc] init]` で生成したインスタンスを `autorelease` して返す。

## References
- [`WKWebpagePreferencesInternal.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesInternal.h#L51)
- [`WKWebpagePreferences.mm#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L176)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
