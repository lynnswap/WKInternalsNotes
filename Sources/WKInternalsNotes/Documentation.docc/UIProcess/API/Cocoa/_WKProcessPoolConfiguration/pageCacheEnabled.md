# ``WKInternalsNotes/_WKProcessPoolConfiguration/pageCacheEnabled``

Back/Forward Cache の有効/無効を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL pageCacheEnabled WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Default Value
既定値は `true`。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `usesBackForwardCache` を直接操作する。

## References
- [`_WKProcessPoolConfiguration.mm#L286`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L286)
- [`_WKProcessPoolConfiguration.mm#L291`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L291)
- [`APIProcessPoolConfiguration.h#L194`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L194)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
