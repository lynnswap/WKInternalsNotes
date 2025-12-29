# ``WKInternalsNotes/_WKAutomationSessionConfiguration/alwaysAllowAutoplay``

自動再生を常に許可するかを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL alwaysAllowAutoplay;
```

## Default Value
`NO`。

## Discussion
`init` で `NO` に初期化され、`copyWithZone:` で現在の値が複製される。

## References
- [`_WKAutomationSessionConfiguration.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionConfiguration.h#L38)
- [`_WKAutomationSessionConfiguration.mm#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSessionConfiguration.mm#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
