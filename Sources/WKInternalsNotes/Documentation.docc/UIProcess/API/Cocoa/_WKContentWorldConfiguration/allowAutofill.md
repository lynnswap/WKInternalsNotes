# ``WKInternalsNotes/_WKContentWorldConfiguration/allowAutofill``

Autofill を許可するかを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL allowAutofill;
```

## Default Value
`NO`。

## Discussion
`WKContentWorld` 生成時に `AllowAutofill` オプションへ反映され、既存の world と値が一致しない場合は例外になる。

## References
- [`WKContentWorld.mm#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorld.mm#L32)
- [`WKContentWorld.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorld.mm#L101)
- [`WKContentWorldConfiguration.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentWorldConfiguration.mm#L53)
- [`_WKContentWorldConfiguration.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKContentWorldConfiguration.h#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
