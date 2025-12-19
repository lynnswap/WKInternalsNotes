# ``WKInternalsNotes/WKContentView/isEditable``

編集可能状態かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isEditable;
```

## Default Value
`_isEditable` を返す。

## Discussion
内部フラグ `_isEditable` を返す単純な getter。

## References
- [`WKContentViewInteraction.h#L543`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L543)
- [`WKContentViewInteraction.mm#L1948`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1948)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
