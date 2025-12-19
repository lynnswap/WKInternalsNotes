# ``WKInternalsNotes/_WKTextManipulationItem/isCrossSiteSubframe``

クロスサイトサブフレーム由来の項目かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isCrossSiteSubframe WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
`initWithIdentifier:tokens:isSubframe:isCrossSiteSubframe:` で渡した値。`initWithIdentifier:tokens:` では `NO`。

## Discussion
`isCrossSiteSubframe` フラグをそのまま返す。

## References
- [`_WKTextManipulationItem.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.h#L43)
- [`_WKTextManipulationItem.mm#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.mm#L58)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
