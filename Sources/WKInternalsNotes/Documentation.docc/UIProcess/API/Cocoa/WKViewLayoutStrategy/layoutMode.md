# ``WKInternalsNotes/WKViewLayoutStrategy/layoutMode``

現在のレイアウトモードを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKLayoutMode layoutMode;
```

## Default Value
`initWithPage:view:viewImpl:mode:` に渡された値が設定される。

## Discussion
getter は `_layoutMode` を返す。

## References
- [`WKViewLayoutStrategy.mm#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L75)
- [`WKViewLayoutStrategy.mm#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L97)
- [`WKViewLayoutStrategy.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.h#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
