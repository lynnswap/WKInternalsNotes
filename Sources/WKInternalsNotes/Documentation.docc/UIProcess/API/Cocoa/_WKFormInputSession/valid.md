# ``WKInternalsNotes/_WKFormInputSession/valid``

入力セッションが有効かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isValid) BOOL valid;
```

## Default Value
初期化直後は `YES`。`invalidate` 後は `NO`。

## Discussion
内部の `_contentView` が存在するかどうかで判定する。`invalidate` で `_contentView` を `nil` にするため以降は `NO` を返す。

## References
- [`WKContentViewInteraction.mm#L797`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L797)
- [`WKContentViewInteraction.mm#L898`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L898)
- [`_WKFormInputSession.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFormInputSession.h#L35)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
