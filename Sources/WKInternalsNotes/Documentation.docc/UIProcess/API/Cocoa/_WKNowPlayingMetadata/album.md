# ``WKInternalsNotes/_WKNowPlayingMetadata/album``

Now Playing のアルバム名を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *album;
```

## Default Value
生成直後は `nil`。`_setNowPlayingMetadataObserver` が発火すると `metadata.album` をコピーして設定する。

## Discussion
テスト用の Now Playing メタデータ観測で `WebCore::NowPlayingMetadata` の `album` を `NSString` に変換し、`setAlbum:` で代入して observer に渡す。`copy` 属性のため渡された文字列をコピー保持する。

## References
- [`WKWebViewPrivateForTesting.h#L237`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L237)
- [`WKWebViewTesting.mm#L294`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L294)
- [`WKWebViewTesting.mm#L298`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L298)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
