# ``WKInternalsNotes/_WKProcessPoolConfiguration/attrStyleEnabled``

attrStyle 機能の有効/無効を ProcessPool 設定に反映する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL attrStyleEnabled WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
既定値は `false`。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `attrStyleEnabled` フラグに直結する。

## References
- [`_WKProcessPoolConfiguration.mm#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L120)
- [`_WKProcessPoolConfiguration.mm#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L125)
- [`APIProcessPoolConfiguration.h#L182`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L182)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
