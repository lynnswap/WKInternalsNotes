# ``WKInternalsNotes/_WKTextManipulationToken/debugDescription``

トークン内容を含む詳細な説明文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, readonly) NSString *debugDescription;
```

## Discussion
`_descriptionPreservingPrivacy:NO` を呼び、`content` と `userInfo` を含む文字列を生成する。

## References
- [`_WKTextManipulationToken.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationToken.h#L44)
- [`_WKTextManipulationToken.mm#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationToken.mm#L100)
- [`_WKTextManipulationToken.mm#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationToken.mm#L105)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
