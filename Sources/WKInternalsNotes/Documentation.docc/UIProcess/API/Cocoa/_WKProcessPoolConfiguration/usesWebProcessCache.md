# ``WKInternalsNotes/_WKProcessPoolConfiguration/usesWebProcessCache``

WebProcess キャッシュの使用を有効/無効にする。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL usesWebProcessCache WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
既定値は `false`。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `usesWebProcessCache` を直接操作する。

## References
- [`_WKProcessPoolConfiguration.mm#L256`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L256)
- [`_WKProcessPoolConfiguration.mm#L261`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L261)
- [`APIProcessPoolConfiguration.h#L193`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L193)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
