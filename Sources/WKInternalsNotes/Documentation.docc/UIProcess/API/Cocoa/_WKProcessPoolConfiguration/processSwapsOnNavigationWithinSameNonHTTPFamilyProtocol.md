# ``WKInternalsNotes/_WKProcessPoolConfiguration/processSwapsOnNavigationWithinSameNonHTTPFamilyProtocol``

同一非 HTTP ファミリープロトコル間でもプロセススワップするかを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL processSwapsOnNavigationWithinSameNonHTTPFamilyProtocol WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
既定値は `false`。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `processSwapsOnNavigationWithinSameNonHTTPFamilyProtocol` を直接操作する。

## References
- [`_WKProcessPoolConfiguration.mm#L276`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L276)
- [`_WKProcessPoolConfiguration.mm#L281`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L281)
- [`APIProcessPoolConfiguration.h#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L191)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
