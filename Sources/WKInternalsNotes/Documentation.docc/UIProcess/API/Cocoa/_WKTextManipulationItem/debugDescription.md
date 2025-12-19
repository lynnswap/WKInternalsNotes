# ``WKInternalsNotes/_WKTextManipulationItem/debugDescription``

トークン内容を含む詳細な説明文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *debugDescription;
```

## Discussion
`_descriptionPreservingPrivacy:NO` を呼び、各トークンの `debugDescription` を組み込んだ文字列を返す。

## References
- [`_WKTextManipulationItem.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.h#L46)
- [`_WKTextManipulationItem.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.mm#L109)
- [`_WKTextManipulationItem.mm#L114`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.mm#L114)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
